# dictionary

#my_dict = {"www.google":"8.8.8.8","www.facebok.com":"7.7.7.7","www.youtube":["5.5.5.5","4.4.4.4"]}
#my_dict2=({"www.net4u.co.il":"88.88.88.88","www.groo.co.il":"33.33.33.33"})

#print(my_dict)
#print(my_dict2)
#my_dict.update(my_dict2)
#print(my_dict)
#print("\nNumber of Entries : " + str(len(my_dict)))
#print(my_dict["www.google"])
#my_dict["www.google"] = "8.8.4.4"
#print(my_dict["www.google"])
#print(my_dict)

dict_names = {"Boris":116000,"Alex":50000,"Evgeniy":135000,"Timor":80000,"Rita":20000}
print(dict_names)
dict_names["Alex"] = 100000
print(dict_names)
dict_names["Danik"]= 5000
#print("\nThe summary is:" + str(dict_names["Boris"]) + str(dict_names["Danik"]))
#print("The sammary is:" + str(dict_names["Boris"] + dict_names["Rita"]))
summay= dict_names["Boris"]+dict_names["Rita"]
print("summary is:"+ str(summay))
dict_names.update({"Emili":summay})
print(dict_names)
print("\nNumber of entries: "+ str(len(dict_names)))
print("idan" in dict_names)
print("Danik" in dict_names)


