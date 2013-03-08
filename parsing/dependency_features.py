'''
Original code by Joao Graca and Andre Martins (2011-2012)
Modified by Jacob Eisenstein (2013) for Georgia Tech CS 4650/7650 NLP
'''
import sys
import numpy as np
from dependency_reader import *
from itertools import chain, combinations
##########Constants#####################
LOWER_LIMIT = -5
UPPER_LIMIT = 8
#End of constants#
class DependencyFeatures():
    '''
    Dependency features class
    '''
    def __init__(self, use_lexical = False, use_distance = False, use_contextual = False):
        self.feat_dict = {}
        self.n_feats = 0

    def create_dictionary(self, instances):
        '''Creates dictionary of features (note: only uses supported features)'''
        self.feat_dict = {}
        self.n_feats = 0
        for instance in instances:
            nw = np.size(instance.words)-1
            heads = instance.heads
            for m in range(1, nw+1):
                h = heads[m]
                self.create_arc_features(instance, h, m, True)

        print "Number of features: {0}".format(self.n_feats)


    def create_features(self, instance):
        '''Creates arc features from an instance.'''
        nw = np.size(instance.words)-1
        feats = np.empty((nw+1, nw+1), dtype=object)
        for h in range(0,nw+1): 
            for m in range(1,nw+1):
                if h == m:
                    feats[h][m] = []
                    continue
                feats[h][m] = self.create_arc_features(instance, h, m)

        return feats

    def create_arc_features(self,instance,h,m,add=False):
        '''
        Create features for arc h-->m
        This is the function you should modify to do the project
        '''
        feature_function = []
        k = 0 #feature counter

        ## Head pos, modifier pos
        f = self.getF((k,instance.pos[h], instance.pos[m]),add)
        feature_function.append(f)
        k +=1

        ## your features go here
        #Distance between head and modifier
        head_modifier_distance = m - h
        head_modifier_distance = UPPER_LIMIT if head_modifier_distance > UPPER_LIMIT else LOWER_LIMIT if head_modifier_distance < LOWER_LIMIT else head_modifier_distance
        f = self.getF((k,head_modifier_distance),add)
        feature_function.append(f)
        k += 1
        
        #Lexical features between word of the head and tag of modifier        
        f = self.getF((k,instance.words[h],instance.pos[m]),add)
        feature_function.append(f)
        k += 1
        
        #Lexical features between word of the modifier and tag of head
        f = self.getF((k,instance.pos[h],instance.words[m]),add)
        feature_function.append(f)
        k += 1
        
        #Bi-lexical features between word of the modifier and word of the head
        f = self.getF((k,instance.words[h],instance.words[m]),add)
        feature_function.append(f)
        k += 1
        
        # Context features
        words_length = len(instance.words)
        #Tag to the left of head
        head_left_tag = "<START>" if h == 0 else instance.pos[h - 1]
         
        #Tag to the right of head
        head_right_tag = "<END>" if h == words_length - 1 else instance.pos[h + 1]
        
        #Tag to the left of the modifier
        modifier_left_tag = "<START>" if m == 0 else instance.pos[m - 1]
        
        #Tag to the right of the modifier
        modifier_right_tag = "<END>" if m == words_length - 1 else instance.pos[m + 1]
        
        #<t[h]; t[h + k] ; t[m] for k in (1, head_modifier_distance)
        for k in range(1, head_modifier_distance):
            if h!= words_length -1:
                head_rights = instance.pos[h + k]
                temp_f = (instance.pos[h], head_rights, instance.pos[m])
                f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
                feature_function.append(f)
                k += 1

        #<t[h]; t[m - k] ; t[m] for k in (1, head_modifier_distance)
        for k in range(1, head_modifier_distance):
            if m!= 0:
                modifier_lefts = instance.pos[m - k]
                temp_f = (instance.pos[h], modifier_lefts, instance.pos[m])
                f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
                feature_function.append(f)
                k += 1
                

        #<t[h]; t[h - 1]; t[m]>
        temp_f = (instance.pos[h], head_left_tag, instance.pos[m])
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1
        
        #<t[h]; t[m]; t[m + 1]>
        temp_f = (instance.pos[h], instance.pos[m], modifier_right_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1
        
        #<t[h]; t[h - 1]; t[m]; t[m + 1]>
        temp_f = (instance.pos[h], head_left_tag, instance.pos[m], modifier_right_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1

        #<t[h]; t[h + 1]; t[m]; t[m + 1]>
        temp_f = (instance.pos[h], head_right_tag, instance.pos[m], modifier_right_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1
        
        #<t[h]; t[h + 1]; t[m]; t[m - 1]>
        temp_f = (instance.pos[h], head_right_tag, instance.pos[m], modifier_left_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1

        #<t[h]; t[h - 1]; t[m]; t[m - 1]>
        temp_f = (instance.pos[h], head_left_tag, instance.pos[m], modifier_left_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1


        #<t[h]; t[h - 1]; t[h + 1]; t[m]; t[m + 1]>
        temp_f = (instance.pos[h], head_left_tag, head_right_tag, instance.pos[m], modifier_right_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1

        #<t[h]; t[h - 1]; t[h + 1]; t[m]; t[m - 1]>
        temp_f = (instance.pos[h], head_left_tag, head_right_tag, instance.pos[m], modifier_left_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1
        
        #<t[h]; t[m - 1]; t[m]>
        temp_f = (instance.pos[h], modifier_left_tag, instance.pos[m])
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1
        
        #<t[h]; t[h - 1]; t[h + 1]; t[m-1]; t[m]; t[m + 1]>
        temp_f = (instance.pos[h], head_left_tag, head_right_tag, modifier_left_tag, instance.pos[m], modifier_right_tag)
        f = self.getF((k,instance.pos[h],instance.pos[m])+temp_f, add)        
        feature_function.append(f)
        k += 1

        return(feature_function)

    def getF(self, feats, add=True):
        return self.lookup_fid(feats,add)

    def lookup_fid(self, fname, add=False):
        '''Looks up dictionary for feature ID.'''
        if not fname in self.feat_dict:
            if add:
                fid = self.n_feats
                self.n_feats += 1
                self.feat_dict[fname] = fid
                return fid
            else:
                return -1
        else:
            return self.feat_dict[fname]

    def compute_scores(self, feats, weights):
        '''
        Compute scores by taking the dot product between the feature and weight vector.
        Return numpy array of heads by modifiers
        ''' 
        nw = np.size(feats, 0) - 1
        scores = np.zeros((nw+1, nw+1))
        for h in range(nw+1):
            for m in range(nw+1):
                if feats[h][m] == None:
                    continue
                scores[h][m] = sum([weights[f] for f in feats[h][m] if f>=0])
        return scores


