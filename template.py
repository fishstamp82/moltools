#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Template:
    def __init__(self):
        monomer1_hf_cc_pCDZ  =  \
        [
#Dipole
        [ 0.334578 , -0.592384 , 0.430175 ],
#Alpha
        [[ 3.861254 , -1.271224 , -0.711365  ] ,
         [ -1.271224 , 5.014419 , 0.736731  ] ,
         [ -0.711365 , 0.736731 , 6.765428 ]] ,
#Beta
        [[[ -5.346496 , 5.451527 , 1.234515 ],
          [ 5.451527 , -6.627448 , -3.935797 ],
          [ 1.234515 , -3.935796 , -1.538262 ]],

         [[ 5.451527 , -6.627448 ,  -3.935797 ],
          [ -6.627448 , 13.610069 , 4.816182 ],
          [ -3.935796 , 4.816181 , 4.859196 ]],

         [[ 1.234515 , -3.935797 , -1.538263 ],
          [ -3.935797 , 4.816182 , 4.859198 ],
          [ -1.538263 , 4.859198 , -23.416047 ]]]
         ]

        monomer2_hf_cc_pCDZ  =  \
        [
#Dipole
        [ 0.199591 , -0.481684 , 0.616255 ],
#Alpha
        [[ 6.418170 , 1.279270 , 0.579489  ] ,
         [ 1.279270 , 4.552088 , -0.857882  ] ,
         [ 0.579489 , -0.857882 , 4.261423 ]] ,
#Beta
        [[[ -11.012012 , 5.950673 , -11.806065 ],
          [ 5.950674 , 5.599055 , -3.860620 ],
          [ -11.806066 , -3.860620 , -2.227571 ]],

         [[ 5.950673 , 5.599055 ,  -3.860620 ],
          [ 5.599055 , 10.272574 , -4.663896 ],
          [ -3.860620 , -4.663896 , 2.218040 ]],

         [[ -11.806065 , -3.860620 , -2.227570 ],
          [ -3.860620 , -4.663896 , 2.218040 ],
          [ -2.227570 , 2.218040 , -7.124011 ]]]
         ]




        """ 
        
        Coordinates for this model: 
        theta = 104.5
        r = 0.972

        """
        olav_hf_cc_pVDZ =  \
        [
#Dipole
        [ 0.0, 0.0, 0.814458 ],
#Alpha
        [[ 7.204163 , 0.0 , 0.0  ] ,
         [ 0.0 , 3.034600 , 0.0  ] ,
         [ 0.0 , 0.0 , 5.223948 ]] ,
#Beta
        [[[ 0.0 , 0.0, -18.452810 ],
          [ 0.0 , 0.0, 0.0],
          [ -18.452810 , 0.0, 0.0 ]],

         [[ 0.0 , 0.0, 0.0 ],
          [ 0.0 , 0.0, -2.336562 ],
          [ 0.0 , -2.336562 , 0.0 ]],

         [[ -18.452813 , 0.0, 0.0 ],
          [ 0.0 , -2.336562 , 0.0 ],
          [ 0.0 , 0.0, -11.161749 ]]]
         ]

        centered_b3lyp_cc_pVDZ =  {}

#Template properties for CENTERED, r = 0.958019, theta = 104.5 water
        centered_hf_cc_pVDZ =  \
        [
#Dipole
        [ 0.0, 0.0, 0.809400 ],
#Alpha
        [[ 6.922537 , 0.0 , 0.0  ] ,
         [ 0.0 , 3.040036 , 0.0  ] ,
         [ 0.0 , 0.0 , 5.0931372 ]],
#Beta
        [[[ 0.0 , 0.0, -17.217324 ],
          [ 0.0 , 0.0, 0.0],
          [ -17.217324 , 0.0, 0.0 ]],

         [[ 0.0 , 0.0, 0.0 ],
          [ 0.0 , 0.0, -2.339154 ],
          [ 0.0 , -2.339154 , 0.0 ]],

         [[ -17.217324 , 0.0, 0.0 ],
          [ 0.0 , -2.339154 , 0.0 ],
          [ 0.0 , 0.0, -10.671809 ]]]
         ]

#  TIP3P model HF cc-pVDZ
        tip3p_hf_cc_pVDZ =  \
        [
#Dipole
        [ 0.0, 0.0, 0.808971 ],
#Alpha
        [[ 6.906544 , 0.0 , 0.0 ],
         [ 0.0 , 3.040337 , 0.0 ],
         [ 0.0 , 0.0 ,  5.084489 ]],
#Beta
        [[[ 0.0 , 0.0 , -17.144250 ],
          [ 0.0 , 0.0 , 0.0],
          [ -17.144250 , 0.0, 0.0]],

         [[ 0.0 , 0.0, 0.0],
          [ 0.0 , 0.0, -2.338925 ],
          [ 0.0 , -2.338925 , 0.0 ]],

         [[ -17.144250 , 0.0, 0.0],
          [ 0.0 , -2.338925 , 0.0],
          [ 0.0 , 0.0, -10.640297 ]]]
         ]



#Template properties for CENTERED, r = 0.958019, theta = 104.5 water
        centered_b3lyp_middle =  \
        [
#Dipole
        [ 0.0, 0.0, 0.731498 ],
#Alpha
        [[ 9.326228 , 0.0 , 0.0  ] ,
         [ 0.0 , 9.206878 , 0.0  ] ,
         [ 0.0 , 0.0 , 9.037904 ]],
#Beta
        [[[ 0.0 , 0.0, -9.717288 ],
          [ 0.0 , 0.0, 0.0],
          [ -9.717288 , 0.0, 0.0 ]],

         [[ 0.0 , 0.0, 0.0 ],
          [ 0.0 , 0.0, -3.984672 ],
          [ 0.0 , -3.984672 , 0.0 ]],

         [[ -9.717288 , 0.0, 0.0 ],
          [ 0.0 , -3.984672 , 0.0 ],
          [ 0.0 , 0.0, -4.716134 ]]]
         ]


#  TIP3P model
        tip3p_b3lyp_middle =  \
        [
#Dipole
        [ 0.0, 0.0, 0.731575 ],
#Alpha
        [[ 9.333366 , 0.0 , 0.0 ],
         [ 0.0 , 9.208982 , 0.0 ],
         [ 0.0 , 0.0 ,  9.042354 ]],
#Beta
        [[[ 0.0 , 0.0 , -9.744865 ],
          [ 0.0 , 0.0 , 0.0],
          [ -9.744865 , 0.0, 0.0]],

         [[ 0.0 , 0.0, 0.0],
          [ 0.0 , 0.0, -3.975595 ],
          [ 0.0 , -3.975595 , 0.0 ]],

         [[ -9.744865 , 0.0, 0.0],
          [ 0.0 , -3.975595 , 0.0],
          [ 0.0 , 0.0, -4.716610 ]]]
         ]

# SPC water model
# HF
        spc_hf_cc_pVDZ =  \
        [
#Dipole
        [ 0.0, 0.0, 0.792907 ],
#Alpha
        [[ 7.985773 , 0.0 , 0.0  ] ,
         [ 0.0 , 3.019117 , 0.0  ] ,
         [ 0.0 , 0.0 , 5.245267 ]],
#Beta
        [[[ 0.0 , 0.0, -20.972694 ],
          [ 0.0 , 0.0, 0.0],
          [ -20.972694 , 0.0, 0.0 ]],

         [[ 0.0 , 0.0, 0.0 ],
          [ 0.0 , 0.0, -2.232938 ],
          [ 0.0 , -2.232938 , 0.0 ]],

         [[ -20.972694 , 0.0, 0.0],
          [ 0.0 , -2.232938 , 0.0],
          [ 0.0 , 0.0, -11.478545 ]]]
         ]
        spc_b3lyp_middle =  \
        [
#Dipole
        [ 0.0, 0.0, 0.707846 ],
#Alpha
        [[ 10.301482 , 0.0 , 0.0  ] ,
         [ 0.0 , 9.462288 , 0.0  ] ,
         [ 0.0 , 0.0 , 9.493345 ]],
#Beta
        [[[ 0.0 , 0.0, -13.567895 ],
          [ 0.0 , 0.0, 0.0],
          [ -13.567895 , 0.0, 0.0 ]],

         [[ 0.0 , 0.0, 0.0 ],
          [ 0.0 , 0.0, -2.959169 ],
          [ 0.0 , -2.959170 , 0.0 ]],

         [[ -13.567895 , 0.0, 0.0],
          [ 0.0 , -2.959169 , 0.0],
          [ 0.0 , 0.0, -4.996675 ]]]
         ]

    #Dictionaries from basis
        olav_hf_dict = { "PVDZ" : olav_hf_cc_pVDZ }
        centered_b3lyp_dict = { "MIDDLE" : centered_b3lyp_middle,
                "PVDZ" : centered_b3lyp_cc_pVDZ  }
        centered_hf_dict = { "PVDZ" : centered_hf_cc_pVDZ }
        tip3p_b3lyp_dict = { "MIDDLE" : tip3p_b3lyp_middle }
        tip3p_hf_dict = { "PVDZ" : tip3p_hf_cc_pVDZ }
        spc_b3lyp_dict = { "MIDDLE" : spc_b3lyp_middle }
        spc_hf_dict = { "PVDZ" : spc_hf_cc_pVDZ  }

        monomer1_hf_dict = { "PVDZ" : monomer1_hf_cc_pCDZ }
        monomer2_hf_dict = { "PVDZ" : monomer2_hf_cc_pCDZ }

    #Dictionaries from method
        olav_method_dict = { "HF" : olav_hf_dict }
        centered_method_dict = { "B3LYP" : centered_b3lyp_dict,
                "HF" : centered_hf_dict }
        tip3p_method_dict = { "B3LYP" : tip3p_b3lyp_dict,
                "HF" : tip3p_hf_dict }
        spc_method_dict = { "B3LYP": spc_b3lyp_dict, 
                "HF" : spc_hf_dict }
        monomer1_method_dict = { "HF" : monomer1_hf_dict }
        monomer2_method_dict = { "HF" : monomer2_hf_dict }

        self.nameDict = { "OLAV" : olav_method_dict ,
                "MON1" : monomer1_method_dict,
                "MON2" : monomer2_method_dict,
                "CENTERED" : centered_method_dict, \
                "TIP3P": tip3p_method_dict, \
                "SPC" : spc_method_dict }
    def getData(self, model, method, basis):
        return self.nameDict[model][method][basis]

if __name__ == '__main__':
    #Perform tests om Tempaltes
    pass
   
