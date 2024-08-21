package com.itheima;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

//@SpringBootTest
class TliasWebManagementApplicationTests {

    @Test
    void testGenJwt() {
        Map<String,Object> claims=new HashMap<>();
        claims.put("id",1);
        claims.put("name","tom");
        String jwt = Jwts.builder()
                .signWith(SignatureAlgorithm.HS256,"itheima123")
                .setClaims(claims)
                .setExpiration(new Date(System.currentTimeMillis()+3600*1000))
                .compact();
        System.out.println(jwt);
    }
//
    @Test
    public void testParseJwt(){
        Claims claims = Jwts.parser()
                .setSigningKey("apphcsy")
                .parseClaimsJws("eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiaGNzeSIsImlkIjoxLCJleHAiOjE3MTk2NTM0MTJ9.kHmL9F7HZp_2VimENM6G6TUgSnrSebzw9VEwDq2uJu4")
                .getBody();
        System.out.println(claims);
    }
}
