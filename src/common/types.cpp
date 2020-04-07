#include "types.h"
#include <boost/algorithm/string/join.hpp>

double SIFT_Descriptor_weight_map_L2_Distance(const SIFT_Descriptor_weight_map& m1, const SIFT_Descriptor_weight_map& m2){
    return 0.0;
}

std::string split_SIFT_Vector(const SIFT_Vector& descs){
    std::vector<std::string> desc_strs;
    transform(descs.begin(), descs.end(), desc_strs.begin(), [](const SIFT_Descriptor& d) -> std::string{
            return std::string((char*) d.data(), 128);
    });
    return boost::algorithm::join(desc_strs, ",");
}