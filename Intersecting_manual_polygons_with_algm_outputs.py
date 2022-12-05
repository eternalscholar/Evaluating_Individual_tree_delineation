import arcpy
import pandas as pd
import arcgis
import os

arcpy.env.addOutputsToMap = False

arcpy.env.overwriteOutput = True


root_folder_list_case1 = [r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Li_classified",  r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Li_unclassified",
                   r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Da_classified", r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Da_unclassified",
                   r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Si_classified", r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Si_unclassified"]
algm_list = ["Li", "Li", "Da", "Da", "Si", "Si"]
csv_filepath_list_case1 = [r"C:\Study_2\With_classification\Median_IoU_Results_Li_Trees-near-Buildings_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Li_Trees-near-Buildings_unclassified.csv",
                    r"C:\Study_2\With_classification\Median_IoU_Results_Da_Trees-near-Buildings_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Da_Trees-near-Buildings_unclassified.csv",
                    r"C:\Study_2\With_classification\Median_IoU_Results_Si_Trees-near-Buildings_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Si_Trees-near-Buildings_unclassified.csv"]
man_file_case1 = r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings.shp"



root_folder_list_case2 = [r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Li_classified", r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Li_unclassified",
                         r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Da_classified", r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Da_unclassified", 
                          r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Si_classified", r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Si_unclassified"]
csv_filepath_list_case2 = [r"C:\Study_2\With_classification\Median_IoU_Results_Li_Manmade_objects_near_trees_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Li_Manmade_objects_near_trees_unclassified.csv",
                          r"C:\Study_2\With_classification\Median_IoU_Results_Da_Manmade_objects_near_trees_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Da_Manmade_objects_near_trees_unclassified.csv", 
                          r"C:\Study_2\With_classification\Median_IoU_Results_Si_Manmade_objects_near_trees_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Si_Manmade_objects_near_trees_unclassified.csv"]
man_file_case2 = r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_trees_hand_drawn\Individual_trees_hand_drawn_manmade_obj_near_trees.shp"

# for j in range(0,6):
#     root_folder = root_folder_list_case1[j]
#     csv_filepath = csv_filepath_list_case1[j]
#     algm = algm_list[j]
#     man_file = man_file_case1
#     folders_list = [x[0] for x in os.walk(root_folder)]

#     id_manual = "ID_Manual"
#     for i in range(1,len(folders_list)):
#     #for i in range(23,len(folders_list)):
#         algm_Out_Folder = os.path.join(root_folder, folders_list[i]) 
#         out_merge_file_name = algm + "_individual_canopies_merged_" + str(i) + ".shp"
#         out_intersect_file_name = "Man_" + algm + "_intersect_" + str(i) + ".shp"
# #         print(algm_Out_Folder)


#         id_field = "ID_" + algm
#         area_field = "Area"+ algm
#         id_field_inter = "ID_" + algm + "_m"
#         area_field_inter = "Area"+ algm + "M"
#         man_Area = "Man_A_whol"

#         final_out_intersect_file_name = "final_"+ out_intersect_file_name
#         #man_file = r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings.shp"

#         #Merging individual files into one shapefile
#         out_merge_full_path = os.path.join(algm_Out_Folder, out_merge_file_name)
#         out_intersect_full_path = os.path.join(algm_Out_Folder, out_intersect_file_name)
#         final_out_intersect_full_path = os.path.join(algm_Out_Folder, final_out_intersect_file_name)
#         file_list = []
#         for file in os.listdir(algm_Out_Folder):
#             if (file.endswith(".shp")):
#                 file_list.append(os.path.join(algm_Out_Folder, file))        
                
# #         for file in os.listdir(algm_Out_Folder):
# #             if ('final' in file):
# #                 in_file = os.path.join(algm_Out_Folder, file)
# #                 in_file_ext = os.path.splitext(in_file)[1]
# #                 out_file_basename = os.path.splitext(final_out_intersect_full_path)[0]
# #                 out_file_path = out_file_basename + in_file_ext
# #                 os.rename(in_file, out_file_path)
                
# #             elif 'merged' in file:
# #                 in_file = os.path.join(algm_Out_Folder, file)
# #                 in_file_ext = os.path.splitext(in_file)[1]
# #                 out_file_basename = os.path.splitext(out_merge_full_path)[0]
# #                 out_file_path = out_file_basename + in_file_ext
# #                 os.rename(in_file, out_file_path)
# #             elif (('intersect' in file) and (not ('final' in file)):
# #                 in_file = os.path.join(algm_Out_Folder, file)
# #                 in_file_ext = os.path.splitext(in_file)[1]
# #                 out_file_basename = os.path.splitext(out_intersect_full_path)[0]
# #                 out_file_path = out_file_basename + in_file_ext
# #                 os.rename(in_file, out_file_path)
# #             else:
# #                   print("No renaming")
# #             if (file.endswith(".shp")):
# #                 file_list.append(os.path.join(algm_Out_Folder, file))
        
#         if (not os.path.exists(out_merge_full_path)):
#             arcpy.management.Merge(file_list, out_merge_full_path)

#             #Adding fields
#             arcpy.management.AddField(out_merge_full_path, id_field, field_type = "SHORT")
#             arcpy.management.AddField(out_merge_full_path, area_field, field_type = "FLOAT")
#             arcpy.management.CalculateField(out_merge_full_path, id_field, '!FID!')
#             arcpy.management.CalculateField(out_merge_full_path, area_field, '!SHAPE.area!')

#             #Creating empty feature class for intersection
#             arcpy.management.CreateFeatureclass(algm_Out_Folder, out_intersect_file_name, 'POLYGON')


#         #Intersection
#         if (not os.path.exists(out_intersect_file_name)):

#             arcpy.analysis.PairwiseIntersect([man_file, out_merge_full_path], out_intersect_full_path)

#             #Adding fields
#             arcpy.management.AddField(out_intersect_full_path, id_field_inter, field_type = "SHORT")
#             arcpy.management.AddField(out_intersect_full_path, area_field_inter, field_type = "FLOAT")
#             arcpy.management.CalculateField(out_intersect_full_path, id_field_inter, '!FID!')
#             arcpy.management.CalculateField(out_intersect_full_path, area_field_inter, '!SHAPE.area!')

#         #Spatial dataframe operations
#         sdf = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
#         sdf_merge = pd.DataFrame.spatial.from_featureclass(out_merge_full_path)
#         num_poly = sdf_merge.shape[0]
#         new_sdf = sdf.loc[sdf.groupby(id_manual)[area_field_inter].idxmax()]
#         new_sdf["IoU"] = new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] - new_sdf[area_field_inter])
#         new_sdf["Dice_coef"] = 2 * new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] )
#         new_sdf.spatial.to_featureclass(final_out_intersect_full_path, sanitize_columns = False)
#         sdf_handdrawn = pd.DataFrame.spatial.from_featureclass(man_file)
#         sdf_intersect = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
#         num_of_Handdrawn_poly = sdf_handdrawn.shape[0]
#         num_of_poly_inside_Handdrawn_poly = sdf_intersect.shape[0]
#         overseg_factor = num_of_Handdrawn_poly / num_of_poly_inside_Handdrawn_poly
#         delineaton_factor = num_of_Handdrawn_poly / num_poly
#         weight_IoU = 0.25
#         weight_Dice = 0.25
#         weight_overseg_factor = 0.25
#         weight_num_of_poly = 0.25
#         Median_IoU = new_sdf["IoU"].median()
#         Median_Dice = new_sdf["Dice_coef"].median()
#         Total_score = weight_IoU * Median_IoU + weight_Dice * Median_Dice + weight_overseg_factor * overseg_factor + weight_num_of_poly * delineaton_factor
        
        
#         #results_df = pd.read_csv(r"C:\Study_2\Median_IoU_Results.csv")
#         df2 = {'Folder_Name': algm_Out_Folder, 'Median_IoU':Median_IoU, 'Median_Dice':Median_Dice, 'overseg_factor':overseg_factor, 'delineaton_factor': delineaton_factor, 
#                'Number_of_polygons':num_poly, 'num_of_Handdrawn_poly': num_of_Handdrawn_poly, 'num_of_poly_inside_Handdrawn_poly': num_of_poly_inside_Handdrawn_poly,
#                'weight_IoU':weight_IoU, 'weight_Dice': weight_Dice, 'weight_overseg_factor': weight_overseg_factor, 
#               'weight_num_of_poly':weight_num_of_poly, 'Total_score': Total_score  }
        
#         #results_df.append(df2, ignore_index = True)
#         result = pd.DataFrame(df2, index = [5])
#         result.to_csv(csv_filepath, mode = 'a', index=True, header=False)
#         print("Wrote {0}".format(csv_filepath))
        

       
        
        
        
for j in range(0,6):
    root_folder = root_folder_list_case2[j]
    csv_filepath = csv_filepath_list_case2[j]
    algm = algm_list[j]
    man_file = man_file_case2
    folders_list = [x[0] for x in os.walk(root_folder)]

    id_manual = "ID_Manual"
    for i in range(1,len(folders_list)):
    #for i in range(23,len(folders_list)):
        algm_Out_Folder = os.path.join(root_folder, folders_list[i]) 
        out_merge_file_name = algm + "_individual_canopies_merged_" + str(i) + ".shp"
        out_intersect_file_name = "Man_" + algm + "_intersect_" + str(i) + ".shp"
#         print(algm_Out_Folder)


        id_field = "ID_" + algm
        area_field = "Area"+ algm
        id_field_inter = "ID_" + algm + "_m"
        area_field_inter = "Area"+ algm + "M"
        man_Area = "Man_A_whol"

        final_out_intersect_file_name = "final_"+ out_intersect_file_name
        #man_file = r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings.shp"

        #Merging individual files into one shapefile
        out_merge_full_path = os.path.join(algm_Out_Folder, out_merge_file_name)
        out_intersect_full_path = os.path.join(algm_Out_Folder, out_intersect_file_name)
        final_out_intersect_full_path = os.path.join(algm_Out_Folder, final_out_intersect_file_name)
        file_list = []
        for file in os.listdir(algm_Out_Folder):
            if (file.endswith(".shp")):
                file_list.append(os.path.join(algm_Out_Folder, file))        
                
#         for file in os.listdir(algm_Out_Folder):
#             if ('final' in file):
#                 in_file = os.path.join(algm_Out_Folder, file)
#                 in_file_ext = os.path.splitext(in_file)[1]
#                 out_file_basename = os.path.splitext(final_out_intersect_full_path)[0]
#                 out_file_path = out_file_basename + in_file_ext
#                 os.rename(in_file, out_file_path)
                
#             elif 'merged' in file:
#                 in_file = os.path.join(algm_Out_Folder, file)
#                 in_file_ext = os.path.splitext(in_file)[1]
#                 out_file_basename = os.path.splitext(out_merge_full_path)[0]
#                 out_file_path = out_file_basename + in_file_ext
#                 os.rename(in_file, out_file_path)
#             elif (('intersect' in file) and (not ('final' in file)):
#                 in_file = os.path.join(algm_Out_Folder, file)
#                 in_file_ext = os.path.splitext(in_file)[1]
#                 out_file_basename = os.path.splitext(out_intersect_full_path)[0]
#                 out_file_path = out_file_basename + in_file_ext
#                 os.rename(in_file, out_file_path)
#             else:
#                   print("No renaming")
#             if (file.endswith(".shp")):
#                 file_list.append(os.path.join(algm_Out_Folder, file))
        
        if (not os.path.exists(out_merge_full_path)):
            arcpy.management.Merge(file_list, out_merge_full_path)

            #Adding fields
            arcpy.management.AddField(out_merge_full_path, id_field, field_type = "SHORT")
            arcpy.management.AddField(out_merge_full_path, area_field, field_type = "FLOAT")
            arcpy.management.CalculateField(out_merge_full_path, id_field, '!FID!')
            arcpy.management.CalculateField(out_merge_full_path, area_field, '!SHAPE.area!')

            #Creating empty feature class for intersection
            arcpy.management.CreateFeatureclass(algm_Out_Folder, out_intersect_file_name, 'POLYGON')


        #Intersection
        if (not os.path.exists(out_intersect_file_name)):

            arcpy.analysis.PairwiseIntersect([man_file, out_merge_full_path], out_intersect_full_path)

            #Adding fields
            arcpy.management.AddField(out_intersect_full_path, id_field_inter, field_type = "SHORT")
            arcpy.management.AddField(out_intersect_full_path, area_field_inter, field_type = "FLOAT")
            arcpy.management.CalculateField(out_intersect_full_path, id_field_inter, '!FID!')
            arcpy.management.CalculateField(out_intersect_full_path, area_field_inter, '!SHAPE.area!')

        #Spatial dataframe operations
        sdf = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
        sdf_merge = pd.DataFrame.spatial.from_featureclass(out_merge_full_path)
        num_poly = sdf_merge.shape[0]
        new_sdf = sdf.loc[sdf.groupby(id_manual)[area_field_inter].idxmax()]
        new_sdf["IoU"] = new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] - new_sdf[area_field_inter])
        new_sdf["Dice_coef"] = 2 * new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] )
        new_sdf.spatial.to_featureclass(final_out_intersect_full_path, sanitize_columns = False)
        sdf_handdrawn = pd.DataFrame.spatial.from_featureclass(man_file)
        sdf_intersect = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
        num_of_Handdrawn_poly = sdf_handdrawn.shape[0]
        num_of_poly_inside_Handdrawn_poly = sdf_intersect.shape[0]
        overseg_factor = num_of_Handdrawn_poly / num_of_poly_inside_Handdrawn_poly
        delineaton_factor = num_of_Handdrawn_poly / num_poly
        weight_IoU = 0.25
        weight_Dice = 0.25
        weight_overseg_factor = 0.25
        weight_num_of_poly = 0.25
        Median_IoU = new_sdf["IoU"].median()
        Median_Dice = new_sdf["Dice_coef"].median()
        Total_score = weight_IoU * Median_IoU + weight_Dice * Median_Dice + weight_overseg_factor * overseg_factor + weight_num_of_poly * delineaton_factor
        
        
        #results_df = pd.read_csv(r"C:\Study_2\Median_IoU_Results.csv")
        df2 = {'Folder_Name': algm_Out_Folder, 'Median_IoU':Median_IoU, 'Median_Dice':Median_Dice, 'overseg_factor':overseg_factor, 'delineaton_factor': delineaton_factor, 
               'Number_of_polygons':num_poly, 'num_of_Handdrawn_poly': num_of_Handdrawn_poly, 'num_of_poly_inside_Handdrawn_poly': num_of_poly_inside_Handdrawn_poly,
               'weight_IoU':weight_IoU, 'weight_Dice': weight_Dice, 'weight_overseg_factor': weight_overseg_factor, 
              'weight_num_of_poly':weight_num_of_poly, 'Total_score': Total_score  }
        
        #results_df.append(df2, ignore_index = True)
        result = pd.DataFrame(df2, index = [5])
        result.to_csv(csv_filepath, mode = 'a', index=True, header=False)
        print("Wrote {0}".format(csv_filepath))


root_folder_list_case1 = [r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Li_classified",  r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Li_unclassified",
                   r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Da_classified", r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Da_unclassified",
                   r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Si_classified", r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_Si_unclassified"]
algm_list = ["Li", "Li", "Da", "Da", "Si", "Si"]
csv_filepath_list_case1 = [r"C:\Study_2\With_classification\Median_IoU_Results_Li_Trees-near-Buildings_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Li_Trees-near-Buildings_unclassified.csv",
                    r"C:\Study_2\With_classification\Median_IoU_Results_Da_Trees-near-Buildings_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Da_Trees-near-Buildings_unclassified.csv",
                    r"C:\Study_2\With_classification\Median_IoU_Results_Si_Trees-near-Buildings_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Si_Trees-near-Buildings_unclassified.csv"]
man_file_case1 = r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings.shp"



root_folder_list_case2 = [r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Li_classified", r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Li_unclassified",
                         r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Da_classified", r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Da_unclassified", 
                          r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Si_classified", r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_tree_canopies_Si_unclassified"]
csv_filepath_list_case2 = [r"C:\Study_2\With_classification\Median_IoU_Results_Li_Manmade_objects_near_trees_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Li_Manmade_objects_near_trees_unclassified.csv",
                          r"C:\Study_2\With_classification\Median_IoU_Results_Da_Manmade_objects_near_trees_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Da_Manmade_objects_near_trees_unclassified.csv", 
                          r"C:\Study_2\With_classification\Median_IoU_Results_Si_Manmade_objects_near_trees_classified.csv", r"C:\Study_2\Without_classification\Median_IoU_Results_Si_Manmade_objects_near_trees_unclassified.csv"]
man_file_case2 = r"C:\Study_2\Shapefiles_larger_iteration\Manmade_objects_near_trees\Individual_trees_hand_drawn\Individual_trees_hand_drawn_manmade_obj_near_trees.shp"

for j in range(5,6):
    root_folder = root_folder_list_case1[j]
    csv_filepath = csv_filepath_list_case1[j]
    algm = algm_list[j]
    man_file = man_file_case1
    folders_list = [x[0] for x in os.walk(root_folder)]

    id_manual = "ID_Manual"
    for i in range(138,len(folders_list)):
    #for i in range(137,len(folders_list)):
        algm_Out_Folder = os.path.join(root_folder, folders_list[i]) 
        out_merge_file_name = algm + "_individual_canopies_merged_" + str(i) + ".shp"
        out_intersect_file_name = "Man_" + algm + "_intersect_" + str(i) + ".shp"
#         print(algm_Out_Folder)


        id_field = "ID_" + algm
        area_field = "Area"+ algm
        id_field_inter = "ID_" + algm + "_m"
        area_field_inter = "Area"+ algm + "M"
        man_Area = "Man_A_whol"

        final_out_intersect_file_name = "final_"+ out_intersect_file_name
        #man_file = r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings.shp"

        #Merging individual files into one shapefile
        out_merge_full_path = os.path.join(algm_Out_Folder, out_merge_file_name)
        out_intersect_full_path = os.path.join(algm_Out_Folder, out_intersect_file_name)
        final_out_intersect_full_path = os.path.join(algm_Out_Folder, final_out_intersect_file_name)
        file_list = []
        for file in os.listdir(algm_Out_Folder):
            if (file.endswith(".shp")):
                file_list.append(os.path.join(algm_Out_Folder, file))        
                
#         for file in os.listdir(algm_Out_Folder):
#             if ('final' in file):
#                 in_file = os.path.join(algm_Out_Folder, file)
#                 in_file_ext = os.path.splitext(in_file)[1]
#                 out_file_basename = os.path.splitext(final_out_intersect_full_path)[0]
#                 out_file_path = out_file_basename + in_file_ext
#                 os.rename(in_file, out_file_path)
                
#             elif 'merged' in file:
#                 in_file = os.path.join(algm_Out_Folder, file)
#                 in_file_ext = os.path.splitext(in_file)[1]
#                 out_file_basename = os.path.splitext(out_merge_full_path)[0]
#                 out_file_path = out_file_basename + in_file_ext
#                 os.rename(in_file, out_file_path)
#             elif (('intersect' in file) and (not ('final' in file)):
#                 in_file = os.path.join(algm_Out_Folder, file)
#                 in_file_ext = os.path.splitext(in_file)[1]
#                 out_file_basename = os.path.splitext(out_intersect_full_path)[0]
#                 out_file_path = out_file_basename + in_file_ext
#                 os.rename(in_file, out_file_path)
#             else:
#                   print("No renaming")
#             if (file.endswith(".shp")):
#                 file_list.append(os.path.join(algm_Out_Folder, file))
        
        if (not os.path.exists(out_merge_full_path)):
            print("inside if")
            arcpy.management.Merge(file_list, out_merge_full_path)

            #Adding fields
            arcpy.management.AddField(out_merge_full_path, id_field, field_type = "SHORT")
            arcpy.management.AddField(out_merge_full_path, area_field, field_type = "FLOAT")
            arcpy.management.CalculateField(out_merge_full_path, id_field, '!FID!')
            arcpy.management.CalculateField(out_merge_full_path, area_field, '!SHAPE.area!')

            #Creating empty feature class for intersection
            arcpy.management.CreateFeatureclass(algm_Out_Folder, out_intersect_file_name, 'POLYGON')


        #Intersection
        if (not os.path.exists(out_intersect_file_name)):

            arcpy.analysis.PairwiseIntersect([man_file, out_merge_full_path], out_intersect_full_path)

            #Adding fields
            arcpy.management.AddField(out_intersect_full_path, id_field_inter, field_type = "SHORT")
            arcpy.management.AddField(out_intersect_full_path, area_field_inter, field_type = "FLOAT")
            arcpy.management.CalculateField(out_intersect_full_path, id_field_inter, '!FID!')
            arcpy.management.CalculateField(out_intersect_full_path, area_field_inter, '!SHAPE.area!')

        #Spatial dataframe operations
        print("out_intersect_full_path {0}".format(out_intersect_full_path))
        print("area_field_inter {0}".format(area_field_inter))
        print("id_manual {0}".format(id_manual))
        sdf = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
        sdf_merge = pd.DataFrame.spatial.from_featureclass(out_merge_full_path)
        num_poly = sdf_merge.shape[0]
        new_sdf = sdf.loc[sdf.groupby(id_manual)[area_field_inter].idxmax()]
        new_sdf["IoU"] = new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] - new_sdf[area_field_inter])
        new_sdf["Dice_coef"] = 2 * new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] )
        new_sdf.spatial.to_featureclass(final_out_intersect_full_path, sanitize_columns = False)
        sdf_handdrawn = pd.DataFrame.spatial.from_featureclass(man_file)
        sdf_intersect = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
        num_of_Handdrawn_poly = sdf_handdrawn.shape[0]
        num_of_poly_inside_Handdrawn_poly = sdf_intersect.shape[0]
        overseg_factor = num_of_Handdrawn_poly / num_of_poly_inside_Handdrawn_poly
        delineaton_factor = num_of_Handdrawn_poly / num_poly
        weight_IoU = 0.25
        weight_Dice = 0.25
        weight_overseg_factor = 0.25
        weight_num_of_poly = 0.25
        Median_IoU = new_sdf["IoU"].median()
        Median_Dice = new_sdf["Dice_coef"].median()
        Total_score = weight_IoU * Median_IoU + weight_Dice * Median_Dice + weight_overseg_factor * overseg_factor + weight_num_of_poly * delineaton_factor
        
        
        #results_df = pd.read_csv(r"C:\Study_2\Median_IoU_Results.csv")
        df2 = {'Folder_Name': algm_Out_Folder, 'Median_IoU':Median_IoU, 'Median_Dice':Median_Dice, 'overseg_factor':overseg_factor, 'delineaton_factor': delineaton_factor, 
               'Number_of_polygons':num_poly, 'num_of_Handdrawn_poly': num_of_Handdrawn_poly, 'num_of_poly_inside_Handdrawn_poly': num_of_poly_inside_Handdrawn_poly,
               'weight_IoU':weight_IoU, 'weight_Dice': weight_Dice, 'weight_overseg_factor': weight_overseg_factor, 
              'weight_num_of_poly':weight_num_of_poly, 'Total_score': Total_score  }
        
        #results_df.append(df2, ignore_index = True)
        result = pd.DataFrame(df2, index = [5])
        result.to_csv(csv_filepath, mode = 'a', index=True, header=False)
        print("Wrote {0}".format(csv_filepath))
        

       
        
        
        
# for j in range(0,6):
#     root_folder = root_folder_list_case2[j]
#     csv_filepath = csv_filepath_list_case2[j]
#     algm = algm_list[j]
#     man_file = man_file_case2
#     folders_list = [x[0] for x in os.walk(root_folder)]

#     id_manual = "ID_Manual"
#     for i in range(1,len(folders_list)):
#     #for i in range(23,len(folders_list)):
#         algm_Out_Folder = os.path.join(root_folder, folders_list[i]) 
#         out_merge_file_name = algm + "_individual_canopies_merged_" + str(i) + ".shp"
#         out_intersect_file_name = "Man_" + algm + "_intersect_" + str(i) + ".shp"
# #         print(algm_Out_Folder)


#         id_field = "ID_" + algm
#         area_field = "Area"+ algm
#         id_field_inter = "ID_" + algm + "_m"
#         area_field_inter = "Area"+ algm + "M"
#         man_Area = "Man_A_whol"

#         final_out_intersect_file_name = "final_"+ out_intersect_file_name
#         #man_file = r"C:\Study_2\Shapefiles_larger_iteration\Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings\Individual_tree_canopies_hand_drawn_Trees_near_buildings.shp"

#         #Merging individual files into one shapefile
#         out_merge_full_path = os.path.join(algm_Out_Folder, out_merge_file_name)
#         out_intersect_full_path = os.path.join(algm_Out_Folder, out_intersect_file_name)
#         final_out_intersect_full_path = os.path.join(algm_Out_Folder, final_out_intersect_file_name)
#         file_list = []
#         for file in os.listdir(algm_Out_Folder):
#             if (file.endswith(".shp")):
#                 file_list.append(os.path.join(algm_Out_Folder, file))        
                
# #         for file in os.listdir(algm_Out_Folder):
# #             if ('final' in file):
# #                 in_file = os.path.join(algm_Out_Folder, file)
# #                 in_file_ext = os.path.splitext(in_file)[1]
# #                 out_file_basename = os.path.splitext(final_out_intersect_full_path)[0]
# #                 out_file_path = out_file_basename + in_file_ext
# #                 os.rename(in_file, out_file_path)
                
# #             elif 'merged' in file:
# #                 in_file = os.path.join(algm_Out_Folder, file)
# #                 in_file_ext = os.path.splitext(in_file)[1]
# #                 out_file_basename = os.path.splitext(out_merge_full_path)[0]
# #                 out_file_path = out_file_basename + in_file_ext
# #                 os.rename(in_file, out_file_path)
# #             elif (('intersect' in file) and (not ('final' in file)):
# #                 in_file = os.path.join(algm_Out_Folder, file)
# #                 in_file_ext = os.path.splitext(in_file)[1]
# #                 out_file_basename = os.path.splitext(out_intersect_full_path)[0]
# #                 out_file_path = out_file_basename + in_file_ext
# #                 os.rename(in_file, out_file_path)
# #             else:
# #                   print("No renaming")
# #             if (file.endswith(".shp")):
# #                 file_list.append(os.path.join(algm_Out_Folder, file))
        
#         if (not os.path.exists(out_merge_full_path)):
#             arcpy.management.Merge(file_list, out_merge_full_path)

#             #Adding fields
#             arcpy.management.AddField(out_merge_full_path, id_field, field_type = "SHORT")
#             arcpy.management.AddField(out_merge_full_path, area_field, field_type = "FLOAT")
#             arcpy.management.CalculateField(out_merge_full_path, id_field, '!FID!')
#             arcpy.management.CalculateField(out_merge_full_path, area_field, '!SHAPE.area!')

#             #Creating empty feature class for intersection
#             arcpy.management.CreateFeatureclass(algm_Out_Folder, out_intersect_file_name, 'POLYGON')


#         #Intersection
#         if (not os.path.exists(out_intersect_file_name)):

#             arcpy.analysis.PairwiseIntersect([man_file, out_merge_full_path], out_intersect_full_path)

#             #Adding fields
#             arcpy.management.AddField(out_intersect_full_path, id_field_inter, field_type = "SHORT")
#             arcpy.management.AddField(out_intersect_full_path, area_field_inter, field_type = "FLOAT")
#             arcpy.management.CalculateField(out_intersect_full_path, id_field_inter, '!FID!')
#             arcpy.management.CalculateField(out_intersect_full_path, area_field_inter, '!SHAPE.area!')

#         #Spatial dataframe operations
#         sdf = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
#         sdf_merge = pd.DataFrame.spatial.from_featureclass(out_merge_full_path)
#         num_poly = sdf_merge.shape[0]
#         new_sdf = sdf.loc[sdf.groupby(id_manual)[area_field_inter].idxmax()]
#         new_sdf["IoU"] = new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] - new_sdf[area_field_inter])
#         new_sdf["Dice_coef"] = 2 * new_sdf[area_field_inter] / (new_sdf[area_field] + new_sdf[man_Area] )
#         new_sdf.spatial.to_featureclass(final_out_intersect_full_path, sanitize_columns = False)
#         sdf_handdrawn = pd.DataFrame.spatial.from_featureclass(man_file)
#         sdf_intersect = pd.DataFrame.spatial.from_featureclass(out_intersect_full_path)
#         num_of_Handdrawn_poly = sdf_handdrawn.shape[0]
#         num_of_poly_inside_Handdrawn_poly = sdf_intersect.shape[0]
#         overseg_factor = num_of_Handdrawn_poly / num_of_poly_inside_Handdrawn_poly
#         delineaton_factor = num_of_Handdrawn_poly / num_poly
#         weight_IoU = 0.25
#         weight_Dice = 0.25
#         weight_overseg_factor = 0.25
#         weight_num_of_poly = 0.25
#         Median_IoU = new_sdf["IoU"].median()
#         Median_Dice = new_sdf["Dice_coef"].median()
#         Total_score = weight_IoU * Median_IoU + weight_Dice * Median_Dice + weight_overseg_factor * overseg_factor + weight_num_of_poly * delineaton_factor
        
        
#         #results_df = pd.read_csv(r"C:\Study_2\Median_IoU_Results.csv")
#         df2 = {'Folder_Name': algm_Out_Folder, 'Median_IoU':Median_IoU, 'Median_Dice':Median_Dice, 'overseg_factor':overseg_factor, 'delineaton_factor': delineaton_factor, 
#                'Number_of_polygons':num_poly, 'num_of_Handdrawn_poly': num_of_Handdrawn_poly, 'num_of_poly_inside_Handdrawn_poly': num_of_poly_inside_Handdrawn_poly,
#                'weight_IoU':weight_IoU, 'weight_Dice': weight_Dice, 'weight_overseg_factor': weight_overseg_factor, 
#               'weight_num_of_poly':weight_num_of_poly, 'Total_score': Total_score  }
        
#         #results_df.append(df2, ignore_index = True)
#         result = pd.DataFrame(df2, index = [5])
#         result.to_csv(csv_filepath, mode = 'a', index=True, header=False)
#         print("Wrote {0}".format(csv_filepath))



out_merge_full_path

print(out_merge_full_path)

print
