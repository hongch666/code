package com.itheima.service;

import com.itheima.pojo.Dept;

import java.util.List;

public interface DeptService {

    List<Dept> list();

    void delete(Integer id) throws Exception;

    void add(Dept dept);

    public void update(Dept dept);

    public Dept getByID(Integer id);
}
