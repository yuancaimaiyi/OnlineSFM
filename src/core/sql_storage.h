#pragma once

#include "mysql_connection.h"
#include <cppconn/resultset.h>
#include <cppconn/prepared_statement.h>
#include "sql_connection_pool.h"

class SQLStorage
{
public:
    SQLStorage();
    sql::ResultSet *IssueQuery(const std::string &q,
                               std::shared_ptr<sql::Connection> con,
                               std::function<void(sql::PreparedStatement *stmt)> modifier);
    void IssueUpdate(const std::string &u,
                     std::function<void(sql::PreparedStatement *stmt)> modifier);
    void IssueUpdate(const std::string &u,
                     std::shared_ptr<sql::Connection> con,
                     std::function<void(sql::PreparedStatement *stmt)> modifier);
    void Execute(const std::string &e, std::function<void(sql::PreparedStatement *stmt)> modifier);
    void Execute(const std::string &ex, std::shared_ptr<sql::Connection> con, std::function<void(sql::PreparedStatement *stmt)> modifier);
    void Transaction(std::function<void(std::shared_ptr<sql::Connection> con)> t,
                     sql::enum_transaction_isolation isolate_level = sql::enum_transaction_isolation::TRANSACTION_REPEATABLE_READ);
    static void InitConnectionPool(unsigned int size);
    virtual ~SQLStorage();

protected:
    ConnectionLoan<sql::Connection> GetConnection();

private:
    static std::unique_ptr<MySQLConnectionPool> _connection_pool;
};