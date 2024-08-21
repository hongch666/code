package com.itheima.controller;

import com.itheima.pojo.Result;
import com.itheima.utils.AliOSSUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.UUID;

@Slf4j
@RestController
public class UploadController {
    @Autowired
    private AliOSSUtils aliOSSUtils;

    //本地存储
    /*@PostMapping("/upload")
    public Result upload(String username, Integer age, MultipartFile image) throws Exception{
        log.info("文件上传:{},{},{}",username,age,image);
        String originalFilename = image.getOriginalFilename();
        //构造唯一的文件名-uuid
        int index=originalFilename.lastIndexOf(".");
        String extname=originalFilename.substring(index);
        String newFilename= UUID.randomUUID().toString()+extname;
        log.info("新的文件名:{}",newFilename);
        image.transferTo(new File("C:\\Users\\红尘岁月\\Desktop\\临时文件夹\\"+newFilename));
        return Result.success();
    }*/
    @PostMapping("/upload")
    public Result upload(MultipartFile image) throws IOException {
        log.info("文件上传,文件名",image.getOriginalFilename());
        //阿里云文件上传
        String url = aliOSSUtils.upload(image);
        log.info("文件上传完成,url为:{}",url);
        return Result.success(url);
    }

}
