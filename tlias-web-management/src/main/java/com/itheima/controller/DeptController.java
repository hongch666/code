package com.itheima.controller;

import com.itheima.anno.Log;
import com.itheima.pojo.Dept;
import com.itheima.pojo.Result;
import com.itheima.service.DeptService;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.logging.Logger;

@Slf4j
@RestController
@RequestMapping("/depts")
public class DeptController {

    //private static Logger log= (Logger) LoggerFactory.getLogger(DeptController.class);

    @Autowired
    private DeptService deptService;

    //@RequestMapping(value = "/depts",method = RequestMethod.GET)//指定请求方式为GET
    @GetMapping
    public Result list(){
        log.info("查询全部部门数据");

        //调用service查询部门信息
        List<Dept> deptList=deptService.list();

        return Result.success(deptList);
    }

    @Log
    @DeleteMapping("/{id}")
    public Result delete(@PathVariable Integer id) throws Exception {
        log.info("根据id删除部门:{}",id);

        deptService.delete(id);

        return Result.success();
    }

    @Log
    @PostMapping
    public Result add(@RequestBody Dept dept){
        log.info("新增部门:{}",dept);

        deptService.add(dept);

        return Result.success();
    }

    @GetMapping("/{id}")
    public Result getByID(@PathVariable Integer id) {
        log.info("获取部门ID:{}",id);
        Dept dept = deptService.getByID(id);
        return Result.success(dept);
    }

    @Log
    @PutMapping
    public Result update(@RequestBody Dept dept) {
        log.info("修改部门:{}",dept);
        deptService.update(dept);
        return Result.success();
    }

}
