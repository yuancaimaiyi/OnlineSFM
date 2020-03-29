#pragma once
#include "openMVG/sfm/sfm_data.hpp"
#include "openMVG/matching/indMatch.hpp"
#include "openMVG/multiview/triangulation_method.hpp"
#include "openMVG/sfm/sfm_data.hpp"
#include "openMVG/numeric/eigen_alias_definition.hpp"
#include "openMVG/cameras/Camera_Common.hpp"
#include "openMVG/sfm/sfm_data.hpp"
#include "openMVG/numeric/eigen_alias_definition.hpp"
#include "openMVG/cameras/Camera_Common.hpp"
#include "openmvg_storage_adapter.h"

#include "reconstruction_agent.h"
#include "camera_intrinsics_storage.h"

#include "configuration_adapter.h"

typedef struct OpenMVGReconstructionAgentConfig {
    std::string features_dir = "",
    sfm_dir = "",
    matches_dir = "",
    root_path = "",
    sOutFile = "";
};

class OpenMVGReconstructionAgent : public ReconstructionAgent{
    public:
        OpenMVGReconstructionAgent(const std::string& reconstruction_id, 
                                   CameraIntrinsicsStorage* intrinsics_storage, 
                                   OpenMVGStorageAdapter* openmvg_storage,
                                   std::shared_ptr<ConfigurationAdapter> configuration_adapter);
        bool IncrementalSFM(const std::set<std::string>& new_images){}
        bool AddImage(const std::string& image_path);
        bool ComputeMatches(const std::set<std::string>& image_pathes);
        bool ComputeFeatures(const std::set<std::string>& image_id);
        bool IncrementalSFM();
        bool ComputeStructure();
        void Load(const std::string& sfm_data);
        void SetConfig(const OpenMVGReconstructionAgentConfig& config);
    private:
        openMVG::Pair_Set _GatherMatchesToCompute(const std::set<std::string>& new_image_paths);
        bool _GenerateImageFeatures(const std::string& image_path);
        OpenMVGReconstructionAgentConfig _config;
        std::unique_ptr<openMVG::sfm::SfM_Data> _sfm_data;
        std::shared_ptr<ConfigurationAdapter> _configuration_adapter;
        CameraIntrinsicsStorage* _intrinsics_storage = nullptr;
        OpenMVGStorageAdapter* _openmvg_storage = nullptr;
        std::string _reconstruction_id;
};