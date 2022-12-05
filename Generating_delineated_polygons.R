library(rLiDAR)
library(lidR)
library(raster)
library(sf)
library(concaveman)


#1.1
# li2012: Trees near buildings
# Parameters and default values dt1 = 5, dt2 = 8, Zu = 15

las_non_overlap <- lidR::readLAS("C:/Study_2/LAS_files/30404_30405_merged_clipped.las", select = "xyzrc", filter = "-keep_class 3 4 5")  #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow--------------
dirname_algm <- "C:/Study_2/Shapefiles_larger_iteration/Trees_near_buildings/Individual_tree_canopies_Li_classified"

# las_non_overlap <- lidR::readLAS("C:/Study_2/LAS_files/30404_30405_merged_clipped.las", select = "xyz")                                   #+++++++++For unclassified, enable this line and the line below. Also, disable the two lines above++++++++++++
# dirname_algm <- "C:/Study_2/Shapefiles_larger_iteration/Trees_near_buildings/Individual_tree_canopies_Li_unclassified"


for (dt1 in seq(3, 22, 2)){
  for (dt2 in seq(8, 27, 2)){
    for (Zu in seq(10, 60, 5)){
      
      
      #plot(las_non_overlap_seg_li2012, color = "treeID")
      
      dirname <- paste(dirname_algm, "/", "Li_", dt1, "_", dt2, "_", Zu, sep ="") 
      if (!file.exists(dirname)){
        dir.create(dirname)
        
        las_non_overlap_seg_li2012 <- segment_trees(las_non_overlap, li2012(dt1 = dt1, dt2 = dt2, R = 0, Zu = Zu, hmin = 2, speed_up = 100))
        for (i in unique(las_non_overlap_seg_li2012$treeID)) {
          print(i)
          if (!is.na(i)){
            tree_point_cloud <- filter_poi(las_non_overlap_seg_li2012, treeID==i)
            tryCatch({
              tree_poly <- st_concave_hull(tree_point_cloud)
              filename <- paste(dirname, "/", i , ".shp", sep ="")
              print(filename)
              st_write(tree_poly, filename)
            }, warning = function(w) {
              print('Warning')
            }, error = function(e) {
              print('error')
            }, finally = {
              
            }
            )
          }
        }
      }
    }
  }
}  





 
  
  
#1.2
#dalponte2016: Trees near buildings
# Parameters and default values lmf_value = 20, th_cr = 0.25, th_seed = 0.25

las_non_overlap <- lidR::readLAS("C:/Study_2/LAS_files/30404_30405_merged_clipped.las", select = "xyzrc", filter = "-keep_class 3 4 5")    #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow-------------
dirname_algm <- "C:/Study_2/Shapefiles_larger_iteration/Trees_near_buildings/Individual_tree_canopies_Da_classified"

# las_non_overlap <- lidR::readLAS("C:/Study_2/LAS_files/30404_30405_merged_clipped.las", select = "xyz")    #+++++++++For unclassified, enable this line and the line below. Also, disable the two lines above ++++++++++++
# dirname_algm <- "C:/Study_2/Shapefiles_larger_iteration/Trees_near_buildings/Individual_tree_canopies_Da_unclassified"

chm <- raster("C:/Study_2/Rasters/Trees_near_buildings/Trees_near_buildings_CHM_1ft_NAD83.tif")

for (lmf_value in seq(5, 34, 3)){
  for (th_cr in seq(0.05, 0.51, 0.05)){
    for (th_seed in seq(0.05, 0.56, 0.05)){
      
      ttops <- locate_trees(chm, lmf(lmf_value))
      las_non_overlap_seg <- segment_trees(las_non_overlap, dalponte2016(chm, ttops, max_cr = 100, th_cr = th_cr, th_seed = th_seed))
      #plot(las_dalponte_v_h_hetero, color = "treeID")

      dirname <- paste(dirname_algm, "/","Da_", lmf_value, "_", th_cr, "_", th_seed, sep ="")
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }


    }
  }
}




#1.3
#Silva2016


las_non_overlap <- lidR::readLAS("C:/Study_2/LAS_files/30404_30405_merged_clipped.las", select = "xyzrc", filter = "-keep_class 3 4 5") #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow------------
dirname_algm <- "C:/Study_2/Shapefiles/Trees_near_buildings/Individual_tree_canopies_Si_classified"

# las_non_overlap <- lidR::readLAS("C:/Study_2/LAS_files/30404_30405_merged_clipped.las", select = "xyz") #+++++++++For unclassified, enable this line and the line below. Also, disable the two lines above ++++++++++++
# dirname_algm <- "C:/Study_2/Shapefiles/Trees_near_buildings/Individual_tree_canopies_Si_unclassified"

chm <- raster("C:/Study_2/Rasters/Trees_near_buildings/Trees_near_buildings_CHM_1ft_NAD83.tif")

for (lmf_value in seq(16, 25, 2)){
  for (max_cr_factor in seq(0.50, 0.71, 0.05)){
    for (exclusion in seq(0.2, 0.41, 0.05)){
      #las_silva_v_h_hetero <- segment_trees(las_non_overlap, silva2016(chm, ttops, max_cr_factor = 0.6, exclusion = 0.3, ID = "treeID"))
      
      ttops <- locate_trees(chm, lmf(lmf_value))
      las_non_overlap_seg <- segment_trees(las_non_overlap, silva2016(chm, ttops, max_cr_factor = max_cr_factor, exclusion = exclusion, ID = "treeID"))
      #plot(las_dalponte_v_h_hetero, color = "treeID")
      
      dirname <- paste(dirname_algm, "/","Si_", lmf_value, "_", max_cr_factor, "_", exclusion, sep ="")
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }

    }
  }
}

#*****************************************************************************************************************

#2.1
# li2012: Trees near buildings
# Parameters and default values dt1 = 5, dt2 = 8, Zu = 15

#las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")  #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow--------------
#dirname_algm <- ""C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Li"

las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyz")                                   #+++++++++For unclassified, enable this line and the line below. Also, disable the two lines above++++++++++++
dirname_algm <- "C:/Study_2/Shapefiles_larger_iteration/Manmade_objects_near_trees/Individual_tree_canopies_Li_unclassified"


for (dt1 in seq(3, 22, 2)){
  for (dt2 in seq(8, 27, 2)){
    for (Zu in seq(10, 60, 5)){
      las_non_overlap_seg_li2012 <- segment_trees(las_non_overlap, li2012(dt1 = dt1, dt2 = dt2, R = 0, Zu = Zu, hmin = 2, speed_up = 100))
      #plot(las_non_overlap_seg_li2012, color = "treeID")
      
      dirname <- paste(dirname_algm, "/", "Li_", dt1, "_", dt2, "_", Zu, sep ="")           
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg_li2012$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg_li2012, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }
    }
  }
}  






las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")  #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow--------------
dirname_algm <- "C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Li_classified"

for (dt1 in seq(3, 22, 2)){
  for (dt2 in seq(8, 27, 2)){
    for (Zu in seq(10, 60, 5)){
      las_non_overlap_seg_li2012 <- segment_trees(las_non_overlap, li2012(dt1 = dt1, dt2 = dt2, R = 0, Zu = Zu, hmin = 2, speed_up = 100))
      #plot(las_non_overlap_seg_li2012, color = "treeID")
      
      dirname <- paste(dirname_algm, "/", "Li_", dt1, "_", dt2, "_", Zu, sep ="")           
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg_li2012$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg_li2012, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }
    }
  }
} 


#2.2
#dalponte2016: Trees near buildings
# Parameters and default values lmf_value = 20, th_cr = 0.25, th_seed = 0.25

las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")    #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow-------------
dirname_algm <- "C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Da_classified"

# las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyz")    #+++++++++For unclassified, enable this line and the line below. Also, disable the two lines above ++++++++++++
# dirname_algm <- "C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Da_unclassified"

chm <- raster("C:/Study_2/Rasters/Manmade_objects_near_trees/CHM_Manmade_objects_near_trees_1ft.tif")

for (lmf_value in seq(16, 25, 2)){
  for (th_cr in seq(0.15, 0.36, 0.05)){
    for (th_seed in seq(0.15, 0.36, 0.05)){
      
      ttops <- locate_trees(chm, lmf(lmf_value))
      las_non_overlap_seg <- segment_trees(las_non_overlap, dalponte2016(chm, ttops, max_cr = 100, th_cr = th_cr, th_seed = th_seed))
      #plot(las_dalponte_v_h_hetero, color = "treeID")
      
      dirname <- paste(dirname_algm, "/","Da_", lmf_value, "_", th_cr, "_", th_seed, sep ="")
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }
      
      
    }
  }
}
#2.3
#Silva2016


las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5") #---------For classified, enable this line and the line below. Also, disable the two lines that immediately follow------------
dirname_algm <- "C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Si_classified"

# las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyz") #+++++++++For unclassified, enable this line and the line below. Also, disable the two lines above ++++++++++++
# dirname_algm <- "C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Si_unclassified"

chm <- raster("C:/Study_2/Rasters/Manmade_objects_near_trees/CHM_Manmade_objects_near_trees_1ft.tif")

for (lmf_value in seq(16, 25, 2)){
  for (max_cr_factor in seq(0.50, 0.71, 0.05)){
    for (exclusion in seq(0.2, 0.41, 0.05)){
      #las_silva_v_h_hetero <- segment_trees(las_non_overlap, silva2016(chm, ttops, max_cr_factor = 0.6, exclusion = 0.3, ID = "treeID"))
      
      ttops <- locate_trees(chm, lmf(lmf_value))
      las_non_overlap_seg <- segment_trees(las_non_overlap, silva2016(chm, ttops, max_cr_factor = max_cr_factor, exclusion = exclusion, ID = "treeID"))
      #plot(las_dalponte_v_h_hetero, color = "treeID")
      
      dirname <- paste(dirname_algm, "/","Si_", lmf_value, "_", max_cr_factor, "_", exclusion, sep ="")
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }
      
    }
  }
}

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#3
#3.1
#With classification, li2012: Manmade objects near buildings

for (dt1 in 4:8){
  for (dt2 in 8:12){
    for (Zu in seq(10, 30, 5)){
      las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")
      las_non_overlap_seg_li2012 <- segment_trees(las_non_overlap, li2012(dt1 = dt1, dt2 = dt2, R = 0, Zu = Zu, hmin = 2, speed_up = 100))
      #plot(las_non_overlap_seg_li2012, color = "treeID")
      
      dirname <- paste("C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Li/Li_", dt1, "_", dt2, "_", Zu, sep ="")
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg_li2012$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg_li2012, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            #filename <- paste("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/Shapefiles/Trees_near_buildings/Individual_tree_canopies_Dalponte/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }
    }
  }
  
}  


#3.2
#With classification, dalponte2016
#las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")
las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")
chm <- raster("C:/Study_2/Rasters/Manmade_objects_near_trees/CHM_Manmade_objects_near_trees_1ft.tif")

for (lmf_value in seq(16, 25, 2)){
  for (th_cr in seq(0.15, 0.36, 0.05)){
    for (th_seed in seq(0.15, 0.36, 0.05)){
      
      ttops <- locate_trees(chm, lmf(lmf_value))
      las_non_overlap_seg <- segment_trees(las_non_overlap, dalponte2016(chm, ttops, max_cr = 100, th_cr = th_cr, th_seed = th_seed))
      #plot(las_dalponte_v_h_hetero, color = "treeID")
      
      dirname <- paste("C:/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Da/Da_", lmf_value, "_", th_cr, "_", th_seed, sep ="")
      dir.create(dirname)
      
      for (i in unique(las_non_overlap_seg$treeID)) {
        print(i)
        if (!is.na(i)){
          tree_point_cloud <- filter_poi(las_non_overlap_seg, treeID==i)
          tryCatch({
            tree_poly <- st_concave_hull(tree_point_cloud)
            filename <- paste(dirname, "/", i , ".shp", sep ="")
            #filename <- paste("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/Shapefiles/Trees_near_buildings/Individual_tree_canopies_Dalponte/", i , ".shp", sep ="")
            print(filename)
            st_write(tree_poly, filename)
          }, warning = function(w) {
            print('Warning')
          }, error = function(e) {
            print('error')
          }, finally = {
            
          }
          )
        }
      }
      
      
    }
  }
}





#3.3
# With classification, silva2016
las_non_overlap <- lidR::readLAS("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/clipped_LAS/30410_1_ver12_clip.las", select = "xyzrc", filter = "-keep_class 3 4 5")
chm <- raster("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/Rasters/Manmade_objects_near_trees/CHM_Manmade_objects_near_trees_1ft.tif")
ttops <- locate_trees(chm, lmf(20))
las_dalponte_v_h_hetero <- segment_trees(las_non_overlap, silva2016(chm, ttops, max_cr_factor = 0.6, exclusion = 0.3, ID = "treeID"))
#col <- pastel.colors(200)
#plot(las_non_overlap_seg, color = "treeID", colorPalette = col)
#plot(las_dalponte_v_h_hetero, color = "treeID")


for (i in unique(las_dalponte_v_h_hetero$treeID)) {
  print(i)
  if (!is.na(i)){
    tree_point_cloud <- filter_poi(las_dalponte_v_h_hetero, treeID==i)
    tryCatch({
      tree_poly <- st_concave_hull(tree_point_cloud)
      filename <- paste("Q:/My Drive/NCSU_Courseware/GIS_895_Research_Credits/Study_2/Shapefiles/Manmade_objects_near_trees/Individual_tree_canopies_Silva2016/", i , ".shp", sep ="")
      print(filename)
      st_write(tree_poly, filename)
    }, warning = function(w) {
      print('Warning')
    }, error = function(e) {
      print('error')
    }, finally = {
      
    }
    )
  }
}



############################################################

