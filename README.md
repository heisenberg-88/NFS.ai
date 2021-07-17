## Implementing self driving car in NFS:MW 2012 sandbox environment using tflearn-Alexnet CNN ,lane detection

latest_ver_2...
Currently in ver_2 , this model behavees better on highways and wide roads with proper lane markings.                                                                            
Accuracy = 93.6 %                                                                                                                                                                  
Validation accuracy = 94.73 %                 AFTER 15 EPOCHS (Due to resource limitations)

RAW FOOTAGE to check how this model behaves:
https://youtu.be/_uycuLdZTN4
https://youtu.be/NkuiH1UMiHs
https://user-images.githubusercontent.com/75937169/126048482-7ba619dd-ebdf-4c0d-ae6a-acba3cbefc49.mp4



![Screenshot 2021-07-18 004016](https://user-images.githubusercontent.com/75937169/126048318-9a9816f6-0f29-4765-96f1-03b62740e6a8.png)


![Screenshot 2021-07-18 004046](https://user-images.githubusercontent.com/75937169/126048319-f24f8fbd-cc5d-4523-922f-5f613efb04ec.png)






## (ver_1) Implementing self driving car in NFS:MW 2012 sandbox environment using tflearn-Alexnet CNN ,lane detection

This is version_1.00 of this project

Accuracy = 91.64 %
Validation accuracy = 91.80 %
  ... this is calculated after 10 epochs.

-> for generating training data , use "training_data_collector.py"  from  "latest_july21" folder.                                                                                 

-> input frames are captured from LEFT-TOP corner of the screen in resolution '800 x 600'.

https://user-images.githubusercontent.com/75937169/126033375-bdea94e9-4a4f-4b4c-81b3-4fb9c482fa89.mp4

## Tensorboard 
![Screenshot 2021-07-16 233651](https://user-images.githubusercontent.com/75937169/125998266-ccf086b8-2776-4f7a-bf14-f0cfd4d2ea91.png)

## accuracy after 10 EPOCHS -> 91.64 %
![Screenshot 2021-07-16 233536](https://user-images.githubusercontent.com/75937169/125998271-c90b5f74-ab9c-415e-982d-16641b29f9c5.png)
